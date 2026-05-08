# CreateCenterLine Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCenterLine`

Obsolete. Superseded by IModelDoc2::CreateCenterLine.
Obsolete. Superseded by [IModelDoc2::CreateCenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLine.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCenterLine( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim P1 As System.Object
Dim P2 As System.Object
Dim value As System.Boolean
 
value = instance.CreateCenterLine(P1, P2)
```

```

System.bool CreateCenterLine( 
   System.object P1,
   System.object P2
)
```

```

System.bool CreateCenterLine( 
   System.Object^ P1,
   System.Object^ P2
) 
```

#### Parameters

*P1*

*P2*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
