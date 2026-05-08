# IGetVertex Method (IExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~IGetVertex`

Obsolete. Superseded by IExtrudeFeatureData2::GetEndConditionReference.
Obsolete. Superseded by [IExtrudeFeatureData2::GetEndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVertex( _
   ByVal Forward As System.Boolean _
) As Vertex
```

```

Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As Vertex
 
value = instance.IGetVertex(Forward)
```

```

Vertex IGetVertex( 
   System.bool Forward
)
```

```

Vertex^ IGetVertex( 
   System.bool Forward
) 
```

#### Parameters

*Forward*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.md)  
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.md)
