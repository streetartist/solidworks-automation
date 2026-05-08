# GetPropertyManagerPage Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyManagerPage`

Obsolete. Superseded by ISldWorks::CreatePropertyManagerPage and ISldWorks::ICreatePropertyManagerPage.
Obsolete. Superseded by [ISldWorks::CreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.md) and [ISldWorks::ICreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.md).

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

Dim instance As IModelDoc2
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
