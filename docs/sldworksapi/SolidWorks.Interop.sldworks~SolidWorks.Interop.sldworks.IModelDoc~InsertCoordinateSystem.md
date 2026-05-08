# InsertCoordinateSystem Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCoordinateSystem`

Obsolete. Superseded by IModelDoc2::InsertCoordinateSystem.
Obsolete. Superseded by [IModelDoc2::InsertCoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCoordinateSystem( _
   ByVal XFlippedIn As System.Boolean, _
   ByVal YFlippedIn As System.Boolean, _
   ByVal ZFlippedIn As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim XFlippedIn As System.Boolean
Dim YFlippedIn As System.Boolean
Dim ZFlippedIn As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertCoordinateSystem(XFlippedIn, YFlippedIn, ZFlippedIn)
```

```

System.bool InsertCoordinateSystem( 
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

```

System.bool InsertCoordinateSystem( 
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
) 
```

#### Parameters

*XFlippedIn*

*YFlippedIn*

*ZFlippedIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
