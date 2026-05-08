# GetOriginalPatternedBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetOriginalPatternedBody`

Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body.
Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOriginalPatternedBody( _
   ByRef Xform As MathTransform _
) As Body2
```

```

Dim instance As IBody2
Dim Xform As MathTransform
Dim value As Body2
 
value = instance.GetOriginalPatternedBody(Xform)
```

```

Body2 GetOriginalPatternedBody( 
   out MathTransform Xform
)
```

```

Body2^ GetOriginalPatternedBody( 
   [Out] MathTransform^ Xform
) 
```

#### Parameters

*Xform*
:   [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

[IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Example

[Get Original Body from Pattern Body (VBA)](Get_Original_Body_from_Pattern_Body_Example_VB.htm)  
[Get Original Body from Pattern Body (VB.NET)](Get_Original_Body_from_Pattern_Body_Example_VBNET.htm)  
[Get Original Body from Pattern Body (C#)](Get_Original_Body_from_Pattern_Body_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
