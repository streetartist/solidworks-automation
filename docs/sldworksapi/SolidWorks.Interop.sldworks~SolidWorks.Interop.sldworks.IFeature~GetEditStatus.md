# GetEditStatus Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetEditStatus`

Gets whether the feature can currently be edited.
Gets whether the feature can currently be edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEditStatus() As System.Integer
```

```

Dim instance As IFeature
Dim value As System.Integer
 
value = instance.GetEditStatus()
```

```

System.int GetEditStatus()
```

```

System.int GetEditStatus(); 
```

#### Return Value

Editing status of feature as defined in [swFeatureEditStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureEditStatus_e.html)

Remarks

Although swFeatureEditStatus\_e is a bitmask, you currently cannot combine its mutually exclusive enumerators and you must examine the bit value of the return value for the editing status of the feature.

|  |  |
| --- | --- |
| **If...** | **Then the return value will be...** |
| a feature and all of its dependent items are not currently being edited | 0 (swFeature\_Editable) for the feature and all of its dependent items |
| a feature is currently being edited | 1 (swFeature\_NonEditable); this will also be the return value for all of the feature's dependent items |
| a sketch is currently being edited | 2 (swFeature\_UnderEditing) |

Example

[Get Editing Status of Features (VB.NET)](Get_Editing_Status_of_Features_Example_VBNET.htm)  
[Get Editing Status of Features (VBA)](Get_Editing_Status_of_Features_Example_VB.htm)  
[Get Editing Status of Features (C#)](Get_Editing_Status_of_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
