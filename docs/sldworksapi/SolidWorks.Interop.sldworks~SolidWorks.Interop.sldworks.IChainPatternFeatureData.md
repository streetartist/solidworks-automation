# IChainPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData`

Allows access to a chain component pattern feature.
Allows access to a chain component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IChainPatternFeatureData 
```

```

Dim instance As IChainPatternFeatureData
```

```

public interface IChainPatternFeatureData 
```

```

public interface class IChainPatternFeatureData 
```

Remarks

This interface supports the following chain component patterns:

- distance
- distance linkage
- connected linkage

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to populate the chain component pattern.

| Entity to select | Corresponding Chain Pattern PropertyManager control | Selection mark | Number of selections |
| --- | --- | --- | --- |
| - 2D or 3D [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) containing an open or closed loop, - [Sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), or - Model [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) | **Path** | 2 | 1 for all types of chain patterns |
| Assembly [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) | **Chain Group 1 Component to Pattern** | 1 | 1 for all types of chain patterns |
| - Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), - Circular or linear edge, - [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), - [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), or - [Reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) | **Chain Group 1 Path Link 1** | 256 | 1 for all types of chain patterns |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 1 Path Link 2** | 512 | - 1 for distance linkage or connected linkage - None for distance |
| Component [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or planar face | **Chain Group 1 Path Alignment Plane** | 16384 | 1 for all types of chain patterns |
| Assembly component | **Chain Group 2 Component to Pattern** | 2048 | - 1 for connected linkage - None for distance or linkage distance |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 2 Path Link 1** | 4096 | - 1 for connected linkage - None for distance or linkage distance |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 2 Path Link 2** | 8192 | - 1 for connected linkage - None for distance or linkage distance |
| Component plane or planar face | **Group 2 Path Alignment Plane** | 32768 | - 1 for connected linkage - None for distance or linkage distance |
| Assembly plane | **Face normal alignment** | 1024 | - 1 if the chain path is a sketch line - None for all other types of paths |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the chain component pattern feature.

Example

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)  
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)  
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
