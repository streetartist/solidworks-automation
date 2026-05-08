# IMultiSelectByRay Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IMultiSelectByRay`

Obsolete. Superseded by IModelDoc2::IMultiSelectByRay.
Obsolete. Superseded by [IModelDoc2::IMultiSelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMultiSelectByRay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMultiSelectByRay( _
   ByRef PointIn As System.Double, _
   ByRef VectorIn As System.Double, _
   ByVal RadiusIn As System.Double, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim PointIn As System.Double
Dim VectorIn As System.Double
Dim RadiusIn As System.Double
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim value As System.Boolean
 
value = instance.IMultiSelectByRay(PointIn, VectorIn, RadiusIn, TypeWanted, Append)
```

```

System.bool IMultiSelectByRay( 
   ref System.double PointIn,
   ref System.double VectorIn,
   System.double RadiusIn,
   System.int TypeWanted,
   System.bool Append
)
```

```

System.bool IMultiSelectByRay( 
   System.double% PointIn,
   System.double% VectorIn,
   System.double RadiusIn,
   System.int TypeWanted,
   System.bool Append
) 
```

#### Parameters

*PointIn*

*VectorIn*

*RadiusIn*

*TypeWanted*

*Append*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
