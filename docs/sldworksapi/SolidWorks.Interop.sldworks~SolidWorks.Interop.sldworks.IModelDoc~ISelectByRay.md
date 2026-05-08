# ISelectByRay Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISelectByRay`

Obsolete. Superseded by IModelDoc2::ISelectByRay.
Obsolete. Superseded by [IModelDoc2::ISelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectByRay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISelectByRay( _
   ByRef PointIn As System.Double, _
   ByRef VectorIn As System.Double, _
   ByVal RadiusIn As System.Double, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim PointIn As System.Double
Dim VectorIn As System.Double
Dim RadiusIn As System.Double
Dim TypeWanted As System.Integer
Dim value As System.Boolean
 
value = instance.ISelectByRay(PointIn, VectorIn, RadiusIn, TypeWanted)
```

```

System.bool ISelectByRay( 
   ref System.double PointIn,
   ref System.double VectorIn,
   System.double RadiusIn,
   System.int TypeWanted
)
```

```

System.bool ISelectByRay( 
   System.double% PointIn,
   System.double% VectorIn,
   System.double RadiusIn,
   System.int TypeWanted
) 
```

#### Parameters

*PointIn*

*VectorIn*

*RadiusIn*

*TypeWanted*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
