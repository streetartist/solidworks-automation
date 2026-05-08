# ICreateBlendSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBlendSurface`

Obsolete. Superseded by IBody2::ICreateBlendSurface.
Obsolete. Superseded by [IBody2::ICreateBlendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBlendSurface.md).

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

Dim instance As IBody
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

*Range1*

*Surface2*

*Range2*

*StartVec*

*EndVec*

*HaveHelpVec*

*HelpVec*

*HaveHelpBox*

*HelpBox*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
