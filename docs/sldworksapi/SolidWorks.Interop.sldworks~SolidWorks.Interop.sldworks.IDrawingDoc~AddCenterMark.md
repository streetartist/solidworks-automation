# AddCenterMark Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddCenterMark`

Obsolete. Superseded by IDrawingDoc::InsertCenterMark2.
Obsolete. Superseded by [IDrawingDoc::InsertCenterMark2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCenterMark( _
   ByVal CmSize As System.Double, _
   ByVal CmShowLines As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim CmSize As System.Double
Dim CmShowLines As System.Boolean
Dim value As System.Boolean
 
value = instance.AddCenterMark(CmSize, CmShowLines)
```

```

System.bool AddCenterMark( 
   System.double CmSize,
   System.bool CmShowLines
)
```

```

System.bool AddCenterMark( 
   System.double CmSize,
   System.bool CmShowLines
) 
```

#### Parameters

*CmSize*

*CmShowLines*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
