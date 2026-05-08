# ITablePatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData`

Allows access to a table-driven pattern feature.
Allows access to a table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ITablePatternFeatureData 
```

```

Dim instance As ITablePatternFeatureData
```

```

public interface ITablePatternFeatureData 
```

```

public interface class ITablePatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the table-driven pattern feature.

| **To** [**select**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)**...** | Use mark... |
| --- | --- |
| Seed feature | 4 |
| Coordinate system | 16 |
| Reference point | 32 |
| Seed face | 128 |
| Seed body | 256 |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the table-driven pattern.

See the **Table Driven Patterns** topic in the SOLIDWORKS user-interface help for more information about table-driven patterns.

Example

'VBA

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\tutorial\api\tablepattern.sldprt**.  
' 2. Delete **TPattern1**.  
' 3. Run the macro.  
' 4. Creates a new **TPattern1**.  
' 5. Inspect the FeatureManager design tree and the graphics area.  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Dim swApp As SldWorks.SldWorks  
Dim swFeatData As TablePatternFeatureData  
Dim Part As SldWorks.ModelDoc2  
Dim swFeat As Feature  
Dim swFeatMgr As FeatureManager  
Dim boolstatus As Boolean

Option Explicit  
Sub main()

> Set swApp = Application.SldWorks  
> Set Part = swApp.ActiveDoc  
>   
> boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 16, Nothing, 0)  
> boolstatus = Part.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)  
> Part.ActivateSelectedFeature  
> Dim swPointArray() As Double  
> ReDim swPointArray(0 To 5) As Double  
> swPointArray(0) = 0.04  
> swPointArray(1) = 0  
> swPointArray(2) = 0  
> swPointArray(3) = -0.025  
> swPointArray(4) = 0  
> swPointArray(5) = 0  
>   
> Set swFeatMgr = Part.FeatureManager  
>   
> Set swFeatData = swFeatMgr.**CreateDefinition**(swFmTablePattern)  
> swFeatData.**GeometryPattern** = False  
> swFeatData.**PointArray** = swPointArray  
> swFeatData.**PropagateVisualProperty** = True  
> swFeatData.**UseCentroid** = True  
> Set swFeat = swFeatMgr.**CreateFeature**(swFeatData)

End Sub

Example

[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)  
[Create Table Pattern (C#)](Create_Table_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
