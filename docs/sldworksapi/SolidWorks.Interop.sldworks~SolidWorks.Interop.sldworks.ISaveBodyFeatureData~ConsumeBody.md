# ConsumeBody Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~ConsumeBody`

Gets or sets whether to consume all bodies in the original part.
Gets or sets whether to consume all bodies in the original part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConsumeBody As System.Boolean
```

```

Dim instance As ISaveBodyFeatureData
Dim value As System.Boolean
 
instance.ConsumeBody = value
 
value = instance.ConsumeBody
```

```

System.bool ConsumeBody {get; set;}
```

```

property System.bool ConsumeBody {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

See **Remarks**

Remarks

**For VBA, .NET:**

True to consume all bodies in the original part, false to not.

**For C++:**

VARIANT\_TRUE (-1) to consume all bodies in the original part, VARIANT\_FALSE (0) to not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)
