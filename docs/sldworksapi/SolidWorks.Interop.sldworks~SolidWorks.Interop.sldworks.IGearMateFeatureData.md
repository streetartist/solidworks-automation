# IGearMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData`

Allows access to gear mate features.
Allows access to gear mate features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IGearMateFeatureData 
```

```

Dim instance As IGearMateFeatureData
```

```

public interface IGearMateFeatureData 
```

```

public interface class IGearMateFeatureData 
```

Remarks

A gear mate forces two components to rotate relative to one another about selected axes.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this mate interface.

To create a gear mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [IGearMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~EntitiesToMate.md) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities using Mark = 1.
3. Specify other properties of the GearMateFeatureData object.

To edit a gear mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a GearMateFeatureData object.
3. Modify the GearMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete a gear mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

'VBA  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\tutorial\api\MechanicalMates\spurgear.sldasm**.  
' 2. Delete **GearMate1** from the Mates folder of the FeatureManager design tree.  
' 3. Run the macro.  
' 4. Inspect the Mates folder in the FeatureManager design tree.  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean

Option Explicit  
Sub main()

> Set swApp = Application.SldWorks  
>   
> Set Part = swApp.ActiveDoc  
>   
> boolstatus = Part.Extension.SelectByRay(-5.60801689982782E-03, -3.24062886681986E-03, -2.52602902980925E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 5.93757005519753E-04, 2, True, 1, 0)  
> boolstatus = Part.Extension.SelectByRay(3.67362652137331E-02, -6.55599730123413E-04, -2.90761848191323E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 5.93757005519753E-04, 2, True, 1, 0)  
>   
> ' Create GearMateFeatureData  
> Dim MateData As SldWorks.GearMateFeatureData  
> Set MateData = Part.**CreateMateData**(10)  
>   
> ' Set the entities To mate  
> Dim EntitiesToMate(1) As Object  
> Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)  
> Dim EntitiesToMateVar As Variant  
> EntitiesToMateVar = EntitiesToMate  
> MateData.**EntitiesToMate** = (EntitiesToMateVar)  
>   
> ' Set the gear ratio numerator  
> MateData.**GearRatioNumerator** = 0.012954  
>   
> ' Set the gear ratio denominator  
> MateData.**GearRatioDenominator** = 0.012954  
>   
> ' Set the mate orientation direction  
> MateData.**Reverse** = False  
>   
> ' Create the mate  
> Dim MateFeature As SldWorks.Feature  
> Set MateFeature = Part.**CreateMate**(MateData)  
> Part.ClearSelection2 True  
> Part.EditRebuild3

End Sub

Example

[Create Gear Mate (C#)](Create_Gear_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
