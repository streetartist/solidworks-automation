# GetButtonPosition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetButtonPosition`

Gets the center coordinates of the specified SOLIDWORKS toolbar button.
Gets the center coordinates of the specified SOLIDWORKS toolbar button.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetButtonPosition( _
   ByVal PointAt As System.Integer, _
   ByRef LocX As System.Integer, _
   ByRef LocY As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim PointAt As System.Integer
Dim LocX As System.Integer
Dim LocY As System.Integer
Dim value As System.Boolean
 
value = instance.GetButtonPosition(PointAt, LocX, LocY)
```

```

System.bool GetButtonPosition( 
   System.int PointAt,
   out System.int LocX,
   out System.int LocY
)
```

```

System.bool GetButtonPosition( 
   System.int PointAt,
   [Out] System.int LocX,
   [Out] System.int LocY
) 
```

#### Parameters

*PointAt*
:   Command ID for SOLIDWORKS toolbar button as defined in [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*LocX*
:   x coordinate of the center of the specified SOLIDWORKS toolbar button

*LocY*
:   y coordinate of the center of the specified SOLIDWORKS toolbar button

#### Return Value

True if method call is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddToolbar5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md)
