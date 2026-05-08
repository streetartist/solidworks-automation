# ICreateEllipse Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateEllipse`

Obsolete. Superseded by IModelDoc2::ICreateEllipse.
Obsolete. Superseded by [IModelDoc2::ICreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateEllipse( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double
 
instance.ICreateEllipse(Center, Major, Minor)
```

```

void ICreateEllipse( 
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor
)
```

```

void ICreateEllipse( 
   System.double% Center,
   System.double% Major,
   System.double% Minor
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

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
