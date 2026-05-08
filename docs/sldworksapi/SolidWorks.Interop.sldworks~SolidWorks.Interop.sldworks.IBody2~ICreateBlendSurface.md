# ICreateBlendSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBlendSurface`

Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces.
Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBlendSurface( _
   ByVal Surface1 As Surface, _
   ByVal Range1 As System.Double, _
   ByVal Surface2 As Surface, _
   ByVal Range2 As System.Double, _
   ByRef StartVec As System.Double, _
   ByRef EndVec As System.Double, _
   ByVal HaveHelpVec As System.Integer, _
   ByRef HelpVec As System.Double, _
   ByVal HaveHelpBox As System.Integer, _
   ByRef HelpBox As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim Surface1 As Surface
Dim Range1 As System.Double
Dim Surface2 As Surface
Dim Range2 As System.Double
Dim StartVec As System.Double
Dim EndVec As System.Double
Dim HaveHelpVec As System.Integer
Dim HelpVec As System.Double
Dim HaveHelpBox As System.Integer
Dim HelpBox As System.Double
Dim value As Surface
 
value = instance.ICreateBlendSurface(Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)
```

```

Surface ICreateBlendSurface( 
   Surface Surface1,
   System.double Range1,
   Surface Surface2,
   System.double Range2,
   ref System.double StartVec,
   ref System.double EndVec,
   System.int HaveHelpVec,
   ref System.double HelpVec,
   System.int HaveHelpBox,
   ref System.double HelpBox
)
```

```

Surface^ ICreateBlendSurface( 
   Surface^ Surface1,
   System.double Range1,
   Surface^ Surface2,
   System.double Range2,
   System.double% StartVec,
   System.double% EndVec,
   System.int HaveHelpVec,
   System.double% HelpVec,
   System.int HaveHelpBox,
   System.double% HelpBox
) 
```

#### Parameters

*Surface1*
:   First side [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

*Range1*
:   Signed offset of Surface1

*Surface2*
:   Second side [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

*Range2*
:   Signed offset of Surface2

*StartVec*
:   Array of 3 doubles representing a point close to the start of the blend spine

*EndVec*
:   Array of 3 doubles representing a point close to the end of the blend spine

*HaveHelpVec*
:   Optional; True if help vector is provided

*HelpVec*
:   Array of 3 doubles representing the direction of the help vector

*HaveHelpBox*
:   Optional; True if box is provided

*HelpBox*
:   Array of 6 doubles bounding the area of interest

#### Return Value

Newly created [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateBlendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBlendSurface.md)
