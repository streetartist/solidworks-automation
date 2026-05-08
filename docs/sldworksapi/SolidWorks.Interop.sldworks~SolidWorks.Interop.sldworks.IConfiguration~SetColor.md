# SetColor Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetColor`

Sets the color for this configuration.
Sets the color for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColor( _
   ByVal ColorIn As System.Integer _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim ColorIn As System.Integer
Dim value As System.Boolean
 
value = instance.SetColor(ColorIn)
```

```

System.bool SetColor( 
   System.int ColorIn
)
```

```

System.bool SetColor( 
   System.int ColorIn
) 
```

#### Parameters

*ColorIn*
:   COLORREF value of the color

#### Return Value

True if the color is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
