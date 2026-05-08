# GetPTZHeight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight`

Obsolete. Superseded by IGtol::GetPTZHeight2.
Obsolete. Superseded by [IGtol::GetPTZHeight2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPTZHeight() As System.String
```

```

Dim instance As IGtol
Dim value As System.String
 
value = instance.GetPTZHeight()
```

```

System.string GetPTZHeight()
```

```

System.String^ GetPTZHeight(); 
```

#### Return Value

Height of the projected tolerance zone (see **Remarks**)

Remarks

This method returns the height of the projected tolerance zone as a string because it is a user-specified parameter that can be textual, numeric, or both types of data.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetPTZHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight.md)
