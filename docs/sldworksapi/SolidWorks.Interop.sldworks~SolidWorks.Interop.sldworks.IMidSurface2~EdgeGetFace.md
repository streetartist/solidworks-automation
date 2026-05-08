# EdgeGetFace Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~EdgeGetFace`

Obsolete. Superseded by IMidSurface3::EdgeGetFace.
Obsolete. Superseded by [IMidSurface3::EdgeGetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~EdgeGetFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EdgeGetFace( _
   ByVal EdgeInDisp As System.Object _
) As System.Object
```

```

Dim instance As IMidSurface2
Dim EdgeInDisp As System.Object
Dim value As System.Object
 
value = instance.EdgeGetFace(EdgeInDisp)
```

```

System.object EdgeGetFace( 
   System.object EdgeInDisp
)
```

```

System.Object^ EdgeGetFace( 
   System.Object^ EdgeInDisp
) 
```

#### Parameters

*EdgeInDisp*
:   Midsurface [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original solid body

Remarks

This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a NULL is returned.

This edge is not topologically related to the face returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::IEdgeGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IEdgeGetFace.md)
