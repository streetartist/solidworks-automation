# LBDownAt Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LBDownAt`

Generates a left mouse button press (down) event.
Generates a left mouse button press (down) event.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub LBDownAt( _
   ByVal Flags As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Flags As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.LBDownAt(Flags, X, Y, Z)
```

```

void LBDownAt( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void LBDownAt( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Flags*
:   Any combination of:

    - MK\_CONTROL
    - MK\_LBUTTON
    - MK\_MBUTTON
    - MK\_RBUTTON
    - MK\_SHIFT

*X*
:   X coordinate of position of cursor

*Y*
:   Y coordinate of position of cursor

*Z*
:   Z coordinate of position of cursor

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::LBUpAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LBUpAt.md)  
[IModelDoc2::DragTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DragTo.md)  
[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.md)
