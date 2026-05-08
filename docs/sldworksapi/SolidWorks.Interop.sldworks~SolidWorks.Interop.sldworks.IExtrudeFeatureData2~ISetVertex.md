# ISetVertex Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetVertex`

Obsolete. Superseded by IExtrudeFeatureData2::SetEndConditionReference.
Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Face As Vertex _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim Face As Vertex
 
instance.ISetVertex(Forward, Face)
```

```

void ISetVertex( 
   System.bool Forward,
   Vertex Face
)
```

```

void ISetVertex( 
   System.bool Forward,
   Vertex^ Face
) 
```

#### Parameters

*Forward*

*Face*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
