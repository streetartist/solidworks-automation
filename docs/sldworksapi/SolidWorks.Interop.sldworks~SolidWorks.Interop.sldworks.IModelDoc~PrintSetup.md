# PrintSetup Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~PrintSetup`

Obsolete. Superseded by IModelDoc2::PrintSetup.
Obsolete. Superseded by [IModelDoc2::PrintSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintSetup.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrintSetup( _
   ByVal SetupType As System.Integer _
) As System.Short
```

```

Dim instance As IModelDoc
Dim SetupType As System.Integer
Dim value As System.Short
 
instance.PrintSetup(SetupType) = value
 
value = instance.PrintSetup(SetupType)
```

```

System.short PrintSetup( 
   System.int SetupType
) {get; set;}
```

```

property System.short PrintSetup {
   System.short get(System.int SetupType);
   void set (System.int SetupType, System.short value);
}
```

#### Parameters

*SetupType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
