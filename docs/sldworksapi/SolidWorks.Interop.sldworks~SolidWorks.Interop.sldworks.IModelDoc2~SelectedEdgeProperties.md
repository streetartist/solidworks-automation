# SelectedEdgeProperties Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties`

Sets the property values of the selected edge.
Sets the property values of the selected edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectedEdgeProperties( _
   ByVal EdgeName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim EdgeName As System.String
Dim value As System.Boolean
 
value = instance.SelectedEdgeProperties(EdgeName)
```

```

System.bool SelectedEdgeProperties( 
   System.string EdgeName
)
```

```

System.bool SelectedEdgeProperties( 
   System.String^ EdgeName
) 
```

#### Parameters

*EdgeName*
:   Name of the edge

#### Return Value

True if edge properties successfully changed, false if not

Remarks

|  |  |
| --- | --- |
| **If the edge...** | **Then this method...** |
| Does not have a name | Sets the name. |
| Has a name | Does not change the name and returns false.  This behavior is intended to prevent a program from renaming an edge that is referenced in some other location.  For example, if an assembly contains a mate to an edge on a part, then a name is automatically assigned to that edge. If you change that name, then there is no guarantee that the mate remains valid. Therefore, when using entity names, you should first check to see if the entity is already named, and if so, use the existing name. If no name exists for the edge, then you can give the edge a name. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SelectedFaceProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFaceProperties.md)  
[IModelDoc2::SelectedFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.md)  
[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IModelDoc2::EntityProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EntityProperties.md)
