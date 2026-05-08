# Move Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~Move`

Moves the mouse pointer in the window space.
Moves the mouse pointer in the window space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Move( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

```

Dim instance As IMouse
Dim X As System.Integer
Dim Y As System.Integer
Dim Flags As System.Integer
Dim value As System.Boolean
 
value = instance.Move(X, Y, Flags)
```

```

System.bool Move( 
   System.int X,
   System.int Y,
   System.int Flags
)
```

```

System.bool Move( 
   System.int X,
   System.int Y,
   System.int Flags
) 
```

#### Parameters

*X*
:   x coordinate where to move the pointer

*Y*
:   y coordinate where to move the pointer

*Flags*
:   Mouse command as defined in [swMouse\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.md) (see **Remarks**)

#### Return Value

True if the pointer moves to the specified position, false if not

Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS *version* Commands type library (substitute the actual SOLIDWORKS version number for *version*) or **SolidWorks.Interop.swcommands.dll**, typically installed in *install\_dir***\api\redist.**

In window space, the origin of the coordinate system is the upper-left corner of the window. Positive x is to the right; positive y is down.

Example

[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)  
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.md)  
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.md)
