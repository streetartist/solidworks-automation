# SetFeatureManagerWidth Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetFeatureManagerWidth`

Sets the width of the FeatureManager design tree.
Sets the width of the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFeatureManagerWidth( _
   ByVal Width As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim Width As System.Integer
Dim value As System.Integer
 
value = instance.SetFeatureManagerWidth(Width)
```

```

System.int SetFeatureManagerWidth( 
   System.int Width
)
```

```

System.int SetFeatureManagerWidth( 
   System.int Width
) 
```

#### Parameters

*Width*
:   Width of the FeatureManager design tree, in pixels

#### Return Value

Status of the set width operation (see **Remarks**)

Remarks

The retval argument indicates the success or failure of the set width operation:

|  |  |
| --- | --- |
| **A value of...** | **Indicates setting of window width...** |
| 0 | Succeeded |
| -1 | Failed |

Example

[Change Width of FeatureManager Design Tree (VBA)](Change_Width_of_FeatureManager_Design_Tree_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetFeatureManagerWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureManagerWidth.md)
