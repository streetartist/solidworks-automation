# IScrewMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData`

Allows access to a screw mate feature.
Allows access to a screw mate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IScrewMateFeatureData 
```

```

Dim instance As IScrewMateFeatureData
```

```

public interface IScrewMateFeatureData 
```

```

public interface class IScrewMateFeatureData 
```

Remarks

A screw mate consists of two components, where:

- Components are concentric.
- Translation of one component along the axis causes rotation of the other component according to a pitch relationship.
- Rotation of one component causes translation of the other component.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this mate interface.

To create a screw mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [IScrewMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~EntitiesToMate.md) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities using Mark = 1.
3. Specify other properties of the ScrewMateFeatureData object. as required.

To edit a screw mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a ScrewMateFeatureData object.
3. Modify the ScrewMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete this screw mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

'VBA

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\tutorial\api\MechanicalMates\Gearbox.sldasm**.  
' 2. Delete Screw2 from the Mates folder of the FeatureManager design tree.  
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
> boolstatus = Part.Extension.SelectByRay(6.13295661213442E-03, 6.89560082602441E-02, 7.45357419147012E-02, -0.540837135649095, -0.258416475165147, -0.800447448659875, 7.89884801245894E-04, 2, True, 1, 0)  
> boolstatus = Part.Extension.SelectByRay(-6.75539884355203E-04, 7.95322044607474E-02, 1.28285894949158E-02, -0.540837135649095, -0.258416475165147, -0.800447448659875, 7.89884801245894E-04, 1, True, 1, 0)  
>   
> ' Create ScrewMateFeatureData  
> Dim MateData As SldWorks.ScrewMateFeatureData  
> Set MateData = Part.**CreateMateData**(17)  
>   
> ' Set the entities To mate  
> Dim EntitiesToMate(1) As Object  
> Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)  
> Dim EntitiesToMateVar As Variant  
> EntitiesToMateVar = EntitiesToMate  
> MateData.**EntitiesToMate** = (EntitiesToMateVar)  
>   
> ' Set the mate revolution type  
> MateData.**RevolutionType** = 0  
>   
> ' Set the mate revolution value  
> MateData.**RevolutionVal** = 1  
>   
> ' Set the mate orientation direction  
> MateData.**Reverse** = True  
>   
> ' Create the mate  
> Dim MateFeature As SldWorks.Feature  
> Set MateFeature = Part.**CreateMate**(MateData)  
> Part.ClearSelection2 True  
> Part.EditRebuild3

End Sub

Example

[Create Screw Mate (C#)](Create_Screw_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
