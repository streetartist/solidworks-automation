# MouseWheelXYZ Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~MouseWheelXYZ`

Zoom in or zoom out using the mouse.
Zoom in or zoom out using the mouse.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MouseWheelXYZ( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Clicks As System.Integer, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

```

Dim instance As IMouse
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Clicks As System.Integer
Dim Flags As System.Integer
Dim value As System.Boolean
 
value = instance.MouseWheelXYZ(X, Y, Z, Clicks, Flags)
```

```

System.bool MouseWheelXYZ( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Clicks,
   System.int Flags
)
```

```

System.bool MouseWheelXYZ( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Clicks,
   System.int Flags
) 
```

#### Parameters

*X*
:   x coordinate where to move the pointer

*Y*
:   y coordinate where to move the pointer

*Z*
:   z coordinate where to move the pointer

*Clicks*
:   Number of clicks to zoom in and out; specify -120 to to zoom in one click and specify 120 to to zoom out

*Flags*
:   Mouse command as defined in [swMouse\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.md) (see **Remarks**)

#### Return Value

True if the operation succeeded, false if not

Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS *version* Commands type library (substitute the actual SOLIDWORKS version number for *version*) or **SolidWorks.Interop.swcommands.dll**, typically installed in *install\_dir***\api\redist.**

The coordinate system is the model's coordinate system.

Example

**Visual Basic for Applications (VBA)**

'--------------------------------  
' Preconditions: Model document is open.  
'  
' Postconditions: Model is zoomed in and out.  
**'--------------------------------**

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelView As SldWorks.ModelView  
Dim swMouse As SldWorks.Mouse

Sub main()

    Set swApp = Application.SldWorks  
    Set swModel = swApp.**ActiveDoc**  
    Set swModelView = swModel.**ActiveView**  
    Set swMouse = swModelView.**GetMouse**

    swMouse.**MouseWheelXYZ** 0, 0, 0, 120, swMouse\_RightUp  
    swMouse.**MouseWheelXYZ** 0, 0, 0, 120, swMouse\_RightUp  
    swMouse.**MouseWheelXYZ** 0, 0, 0, 240, swMouse\_RightUp  
    swMouse.**MouseWheelXYZ** 0, 0, 0, -120, swMouse\_RightUp  
    swMouse.**MouseWheelXYZ** 0, 0, 0, -240, swMouse\_RightUp

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.md)  
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.md)
