# UpdateCutList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList`

Updates an automatically generated cut list.
Updates an automatically generated cut list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateCutList() As System.Boolean
```

```

Dim instance As IBodyFolder
Dim value As System.Boolean
 
value = instance.UpdateCutList()
```

```

System.bool UpdateCutList()
```

```

System.bool UpdateCutList(); 
```

#### Return Value

True if the automatically generated cut list is successfully updated, false if not or because the document does not contain an automatically generated cut list

Remarks

You must specify when to update an automatically generated cut list in a part document. However, an automatically generated cut list in a drawing is automatically updated when you open a drawing that references the cut list.

To find out if the part contains a weldment feature, use [IPartDoc::IsWeldment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsWeldment.md). If it does, then use [IBodyFolder::GetAutomaticCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList.md) to find out if automatic generation of a cut list is enabled.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)  
[IBodyFolder::SetAutomaticCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList.md)  
[IBodyFolder::GetCutListType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.md)
