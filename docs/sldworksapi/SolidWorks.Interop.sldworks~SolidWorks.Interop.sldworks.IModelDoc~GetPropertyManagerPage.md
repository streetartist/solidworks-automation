# GetPropertyManagerPage Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetPropertyManagerPage`

Obsolete. Superseded by IModelDoc2::GetPropertyManagerPage.
Obsolete. Superseded by [IModelDoc2::GetPropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyManagerPage.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPropertyManagerPage( _
   ByVal DialogId As System.Integer, _
   ByVal Title As System.String, _
   ByVal Handler As System.Object _
) As PropertyManagerPage
```

```

Dim instance As IModelDoc
Dim DialogId As System.Integer
Dim Title As System.String
Dim Handler As System.Object
Dim value As PropertyManagerPage
 
value = instance.GetPropertyManagerPage(DialogId, Title, Handler)
```

```

PropertyManagerPage GetPropertyManagerPage( 
   System.int DialogId,
   System.string Title,
   System.object Handler
)
```

```

PropertyManagerPage^ GetPropertyManagerPage( 
   System.int DialogId,
   System.String^ Title,
   System.Object^ Handler
) 
```

#### Parameters

*DialogId*

*Title*

*Handler*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
