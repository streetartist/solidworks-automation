# CreateBlendSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBlendSurface`

Obsolete. Superseded by IBody2::CreateBlendSurface.
Obsolete. Superseded by [IBody2::CreateBlendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBlendSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBlendSurface( _
   ByVal Surface1 As System.Object, _
   ByVal Range1 As System.Double, _
   ByVal Surface2 As System.Object, _
   ByVal Range2 As System.Double, _
   ByVal StartVec As System.Object, _
   ByVal EndVec As System.Object, _
   ByVal HaveHelpVec As System.Integer, _
   ByVal HelpVec As System.Object, _
   ByVal HaveHelpBox As System.Integer, _
   ByVal HelpBox As System.Object _
) As System.Object
```

```

Dim instance As IBody
Dim Surface1 As System.Object
Dim Range1 As System.Double
Dim Surface2 As System.Object
Dim Range2 As System.Double
Dim StartVec As System.Object
Dim EndVec As System.Object
Dim HaveHelpVec As System.Integer
Dim HelpVec As System.Object
Dim HaveHelpBox As System.Integer
Dim HelpBox As System.Object
Dim value As System.Object
 
value = instance.CreateBlendSurface(Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)
```

```

System.object CreateBlendSurface( 
   System.object Surface1,
   System.double Range1,
   System.object Surface2,
   System.double Range2,
   System.object StartVec,
   System.object EndVec,
   System.int HaveHelpVec,
   System.object HelpVec,
   System.int HaveHelpBox,
   System.object HelpBox
)
```

```

System.Object^ CreateBlendSurface( 
   System.Object^ Surface1,
   System.double Range1,
   System.Object^ Surface2,
   System.double Range2,
   System.Object^ StartVec,
   System.Object^ EndVec,
   System.int HaveHelpVec,
   System.Object^ HelpVec,
   System.int HaveHelpBox,
   System.Object^ HelpBox
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
