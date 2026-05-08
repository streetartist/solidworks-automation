# SelectByRay Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectByRay`

Obsolete. Superseded by IModelDoc2::SelectByRay.
Obsolete. Superseded by [IModelDoc2::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByRay(DoubleInfoIn, TypeWanted)
```

```

System.bool SelectByRay( 
   System.object DoubleInfoIn,
   System.int TypeWanted
)
```

```

System.bool SelectByRay( 
   System.Object^ DoubleInfoIn,
   System.int TypeWanted
) 
```

#### Parameters

*DoubleInfoIn*

*TypeWanted*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
