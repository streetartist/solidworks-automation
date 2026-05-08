# MoveXYZ Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~MoveXYZ`

Moves the mouse pointer in the model space.
Moves the mouse pointer in the model space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MoveXYZ( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

```

Dim instance As IMouse
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Flags As System.Integer
Dim value As System.Boolean
 
value = instance.MoveXYZ(X, Y, Z, Flags)
```

```

System.bool MoveXYZ( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Flags
)
```

```

System.bool MoveXYZ( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Flags
) 
```

#### Parameters

*X*
:   x coordinate where to move the pointer

*Y*
:   y coordinate where to move the pointer

*Z*
:   z coordinate where to move the pointer

*Flags*
:   Mouse command as defined in [swMouse\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.md) (see **Remarks**)

#### Return Value

True if the pointer moved to the specified position, false if not

Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS *version* Commands type library (substitute the actual SOLIDWORKS version number for *version*) or **SolidWorks.Interop.swcommands.dll**, typically installed in *install\_dir***\api\redist.**

The coordinate system is the model's coordinate system.

Example

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.md)  
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.md)
