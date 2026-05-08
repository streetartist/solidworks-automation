# ICreatePsplineSurfaceDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreatePsplineSurfaceDLL`

Obsolete. Superseded by IBody2::ICreatePsplineSurfaceDLL.
Obsolete. Superseded by [IBody2::ICreatePsplineSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePsplineSurfaceDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePsplineSurfaceDLL( _
   ByVal Dim As System.Integer, _
   ByVal UOrder As System.Integer, _
   ByVal VOrder As System.Integer, _
   ByVal Ncol As System.Integer, _
   ByVal Nrow As System.Integer, _
   ByRef Coeffs As System.Double, _
   ByVal Basis As System.Integer, _
   ByRef Xform As System.Double, _
   ByVal ScaleFactor As System.Double _
) As Surface
```

```

Dim instance As IBody
Dim Dim As System.Integer
Dim UOrder As System.Integer
Dim VOrder As System.Integer
Dim Ncol As System.Integer
Dim Nrow As System.Integer
Dim Coeffs As System.Double
Dim Basis As System.Integer
Dim Xform As System.Double
Dim ScaleFactor As System.Double
Dim value As Surface
 
value = instance.ICreatePsplineSurfaceDLL(Dim, UOrder, VOrder, Ncol, Nrow, Coeffs, Basis, Xform, ScaleFactor)
```

```

Surface ICreatePsplineSurfaceDLL( 
   System.int Dim,
   System.int UOrder,
   System.int VOrder,
   System.int Ncol,
   System.int Nrow,
   ref System.double Coeffs,
   System.int Basis,
   ref System.double Xform,
   System.double ScaleFactor
)
```

```

Surface^ ICreatePsplineSurfaceDLL( 
   System.int Dim,
   System.int UOrder,
   System.int VOrder,
   System.int Ncol,
   System.int Nrow,
   System.double% Coeffs,
   System.int Basis,
   System.double% Xform,
   System.double ScaleFactor
) 
```

#### Parameters

*Dim*

*UOrder*

*VOrder*

*Ncol*

*Nrow*

*Coeffs*

*Basis*

*Xform*

*ScaleFactor*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
