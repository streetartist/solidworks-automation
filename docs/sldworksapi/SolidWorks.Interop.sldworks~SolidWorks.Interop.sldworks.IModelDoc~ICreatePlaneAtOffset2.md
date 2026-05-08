# ICreatePlaneAtOffset2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePlaneAtOffset2`

Obsolete. Superseded by IModelDoc2::ICreatePlaneAtOffset2.
Obsolete. Superseded by [IModelDoc2::ICreatePlaneAtOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlaneAtOffset2( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
) As RefPlane
```

```

Dim instance As IModelDoc
Dim Val As System.Double
Dim FlipDir As System.Boolean
Dim value As RefPlane
 
value = instance.ICreatePlaneAtOffset2(Val, FlipDir)
```

```

RefPlane ICreatePlaneAtOffset2( 
   System.double Val,
   System.bool FlipDir
)
```

```

RefPlane^ ICreatePlaneAtOffset2( 
   System.double Val,
   System.bool FlipDir
) 
```

#### Parameters

*Val*

*FlipDir*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
