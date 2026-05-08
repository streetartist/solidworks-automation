# FeatureFillet2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureFillet2`

Obsolete. Superseded by IModelDoc2::FeatureFillet2.
Obsolete. Superseded by [IModelDoc2::FeatureFillet2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureFillet2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFillet2( _
   ByVal R1 As System.Double, _
   ByVal Propagate As System.Boolean, _
   ByVal Ftyp As System.Boolean, _
   ByVal VarRadTyp As System.Boolean, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByVal Radii As System.Object _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim R1 As System.Double
Dim Propagate As System.Boolean
Dim Ftyp As System.Boolean
Dim VarRadTyp As System.Boolean
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Object
Dim value As System.Integer
 
value = instance.FeatureFillet2(R1, Propagate, Ftyp, VarRadTyp, OverflowType, NRadii, Radii)
```

```

System.int FeatureFillet2( 
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.object Radii
)
```

```

System.int FeatureFillet2( 
   System.double R1,
   System.bool Propagate,
   System.bool Ftyp,
   System.bool VarRadTyp,
   System.int OverflowType,
   System.int NRadii,
   System.Object^ Radii
) 
```

#### Parameters

*R1*

*Propagate*

*Ftyp*

*VarRadTyp*

*OverflowType*

*NRadii*

*Radii*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
