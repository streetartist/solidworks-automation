# DragTo Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DragTo`

Drags the specified end point.
Drags the specified end point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DragTo( _
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
 
instance.DragTo(Flags, X, Y, Z)
```

```

void DragTo( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void DragTo( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Flags*
:   Mouse-event flags as defined by the operating system. They can be combined to indicate the selection state.  For example:

    - Left-mouse button is pressed: 0x0001
    - Right-mouse button is pressed:  0x0002
    - Shift key is pressed:  0x0004
    - Ctrl key is pressed: 0x0008
    - Middle-mouse button is pressed:  0x0010

*X*
:   X coordinate of end point

*Y*
:   Y coordinate of end point

*Z*
:   Z coordinate of end point

Remarks

This method is only valid for assemblies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
