# IGetMassProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetMassProperties`

Obsolete. Superseded by IModelDoc2::IGetMassProperties.
Obsolete. Superseded by [IModelDoc2::IGetMassProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetMassProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties( _
   ByRef MPropsData As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim MPropsData As System.Double
Dim value As System.Boolean
 
value = instance.IGetMassProperties(MPropsData)
```

```

System.bool IGetMassProperties( 
   ref System.double MPropsData
)
```

```

System.bool IGetMassProperties( 
   System.double% MPropsData
) 
```

#### Parameters

*MPropsData*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
