# SetZoneMargin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneMargin`

Sets the specified zone margin.
Sets the specified zone margin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetZoneMargin( _
   ByVal ZoneMarginType As System.Integer, _
   ByVal MarginValue As System.Double _
) As System.Boolean
```

```

Dim instance As ISheet
Dim ZoneMarginType As System.Integer
Dim MarginValue As System.Double
Dim value As System.Boolean
 
value = instance.SetZoneMargin(ZoneMarginType, MarginValue)
```

```

System.bool SetZoneMargin( 
   System.int ZoneMarginType,
   System.double MarginValue
)
```

```

System.bool SetZoneMargin( 
   System.int ZoneMarginType,
   System.double MarginValue
) 
```

#### Parameters

*ZoneMarginType*
:   Margin type as defined in [swZoneMargin\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneMargin_e.html)

*MarginValue*
:   Margin

#### Return Value

True if zone margin successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
