# PublishFileName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~PublishFileName`

Gets or sets the path and file name to which to export this SOLIDWORKS MBD STEP 242 data.
Gets or sets the path and file name to which to export this SOLIDWORKS MBD STEP 242 data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PublishFileName As System.String
```

```

Dim instance As IMBDSTEP242Data
Dim value As System.String
 
instance.PublishFileName = value
 
value = instance.PublishFileName
```

```

System.string PublishFileName {get; set;}
```

```

property System.String^ PublishFileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Pathname of STEP 242 file (\*.stp)

Example

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md)  
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.md)
