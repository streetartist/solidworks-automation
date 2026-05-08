# IEdgeGetFace Method (IMidSurface3)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IEdgeGetFace`

Gets the body face on which the specified midsurface edge lies.
Gets the body face on which the specified midsurface edge lies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEdgeGetFace( _
   ByVal EdgeInDisp As Edge _
) As Face2
```

```

Dim instance As IMidSurface3
Dim EdgeInDisp As Edge
Dim value As Face2
 
value = instance.IEdgeGetFace(EdgeInDisp)
```

```

Face2 IEdgeGetFace( 
   Edge EdgeInDisp
)
```

```

Face2^ IEdgeGetFace( 
   Edge^ EdgeInDisp
) 
```

#### Parameters

*EdgeInDisp*
:   :   Midsurface [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original solid body

Remarks

This condition occurs when a reference surface extends to meet one of the faces on the original part body. If the edge specified does not lie on one of the original part body faces, then a NULL is returned.

This edge is not topologically related to the face returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)  
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.md)  
[IMidSurface3::EdgeGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~EdgeGetFace.md)
