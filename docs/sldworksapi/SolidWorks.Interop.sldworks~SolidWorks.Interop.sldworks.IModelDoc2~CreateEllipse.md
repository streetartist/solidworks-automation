# CreateEllipse Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse`

Obsolete. Superseded by IModelDoc2::CreateEllipse2.
Obsolete. Superseded by [IModelDoc2::CreateEllipse2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipse( _
   ByVal Center As System.Object, _
   ByVal Major As System.Object, _
   ByVal Minor As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Center As System.Object
Dim Major As System.Object
Dim Minor As System.Object
Dim value As System.Boolean
 
value = instance.CreateEllipse(Center, Major, Minor)
```

```

System.bool CreateEllipse( 
   System.object Center,
   System.object Major,
   System.object Minor
)
```

```

System.bool CreateEllipse( 
   System.Object^ Center,
   System.Object^ Major,
   System.Object^ Minor
) 
```

#### Parameters

*Center*

*Major*

*Minor*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
