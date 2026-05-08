# SketchOffsetEntities2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchOffsetEntities2`

Obsolete. Superseded by IModelDoc2::SketchOffsetEntities2.
Obsolete. Superseded by [IModelDoc2::SketchOffsetEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffsetEntities2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchOffsetEntities2(Offset, BothDirections, Chain)
```

```

System.bool SketchOffsetEntities2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

```

System.bool SketchOffsetEntities2( 
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
) 
```

#### Parameters

*Offset*

*BothDirections*

*Chain*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
