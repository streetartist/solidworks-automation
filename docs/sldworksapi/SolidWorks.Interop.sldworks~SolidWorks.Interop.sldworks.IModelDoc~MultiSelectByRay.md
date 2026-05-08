# MultiSelectByRay Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~MultiSelectByRay`

Obsolete. Superseded by IModelDoc2::MultiSelectByRay.
Obsolete. Superseded by [IModelDoc2::MultiSelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MultiSelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim value As System.Boolean
 
value = instance.MultiSelectByRay(DoubleInfoIn, TypeWanted, Append)
```

```

System.bool MultiSelectByRay( 
   System.object DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
)
```

```

System.bool MultiSelectByRay( 
   System.Object^ DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
) 
```

#### Parameters

*DoubleInfoIn*

*TypeWanted*

*Append*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
