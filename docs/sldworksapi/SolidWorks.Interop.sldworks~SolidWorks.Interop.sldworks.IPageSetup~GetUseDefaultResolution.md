# GetUseDefaultResolution Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetUseDefaultResolution`

Gets whether the printer default resolution is in use on documents and drawing sheets.
Gets whether the printer default resolution is in use on documents and drawing sheets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDefaultResolution() As System.Boolean
```

```

Dim instance As IPageSetup
Dim value As System.Boolean
 
value = instance.GetUseDefaultResolution()
```

```

System.bool GetUseDefaultResolution()
```

```

System.bool GetUseDefaultResolution(); 
```

#### Return Value

True if printer default resolution is in use, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::GetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetResolution.md)  
[IPageSetup::SetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetResolution.md)
