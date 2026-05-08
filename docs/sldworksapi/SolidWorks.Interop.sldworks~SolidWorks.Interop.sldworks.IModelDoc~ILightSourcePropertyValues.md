# ILightSourcePropertyValues Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ILightSourcePropertyValues`

Obsolete. Superseded by IModelDoc2::ILightSourcePropertyValues.
Obsolete. Superseded by [IModelDoc2::ILightSourcePropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ILightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Double
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.Double
 
instance.ILightSourcePropertyValues(ID) = value
 
value = instance.ILightSourcePropertyValues(ID)
```

```

System.double ILightSourcePropertyValues( 
   System.int ID
) {get; set;}
```

```

property System.double ILightSourcePropertyValues {
   System.double get(System.int ID);
   void set (System.int ID, System.double value);
}
```

#### Parameters

*ID*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
