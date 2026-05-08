# GetAutomaticUpdate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticUpdate`

Gets whether to automatically update cut lists.
Gets whether to automatically update cut lists.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutomaticUpdate() As System.Boolean
```

```

Dim instance As IBodyFolder
Dim value As System.Boolean
 
value = instance.GetAutomaticUpdate()
```

```

System.bool GetAutomaticUpdate()
```

```

System.bool GetAutomaticUpdate(); 
```

#### Return Value

True to automatically update cut lists, false to update them manually

Remarks

| To update cut lists... | Call... |
| --- | --- |
| Manually | [IBodyFolder::UpdateCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.md) |
| Automatically | [IBodyFolder::SetAutomaticUpdate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticUpdate.md) |

Example

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)
