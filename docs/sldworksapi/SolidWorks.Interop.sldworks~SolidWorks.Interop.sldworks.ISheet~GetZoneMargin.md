# GetZoneMargin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetZoneMargin`

Gets the specified zone margin.
Gets the specified zone margin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetZoneMargin( _
   ByVal ZoneMargin As System.Integer _
) As System.Double
```

```

Dim instance As ISheet
Dim ZoneMargin As System.Integer
Dim value As System.Double
 
value = instance.GetZoneMargin(ZoneMargin)
```

```

System.double GetZoneMargin( 
   System.int ZoneMargin
)
```

```

System.double GetZoneMargin( 
   System.int ZoneMargin
) 
```

#### Parameters

*ZoneMargin*
:   Margin type to retrieve as defined in [swZoneMargin\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneMargin_e.html)

#### Return Value

Zone margin

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
