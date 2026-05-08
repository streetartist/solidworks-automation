# SetResolution Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetResolution`

Sets the current printer resolution on documents and drawing sheets.
Sets the current printer resolution on documents and drawing sheets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetResolution( _
   ByVal UseDefault As System.Boolean, _
   ByVal DPI As System.Integer _
) As System.Boolean
```

```

Dim instance As IPageSetup
Dim UseDefault As System.Boolean
Dim DPI As System.Integer
Dim value As System.Boolean
 
value = instance.SetResolution(UseDefault, DPI)
```

```

System.bool SetResolution( 
   System.bool UseDefault,
   System.int DPI
)
```

```

System.bool SetResolution( 
   System.bool UseDefault,
   System.int DPI
) 
```

#### Parameters

*UseDefault*
:   True to use the default printer resolution, false to set the printer resolution

*DPI*
:   Dots per inch

#### Return Value

True if printer resolution is set, false if not

Remarks

Specifying IPageSetup::SetResolution (false, 0) turns on the default resolution, which results in [IPageSetup::GetUseDefaultResolution](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetUseDefaultResolution.md) returning True.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::GetResolution Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetResolution.md)
