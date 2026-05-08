# ForceUpdateElectricalData2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ForceUpdateElectricalData2`

Forces an update of electrical data.
Forces an update of electrical data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ForceUpdateElectricalData2( _
   ByVal Stream As System.Integer _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim Stream As System.Integer
Dim value As System.Integer
 
value = instance.ForceUpdateElectricalData2(Stream)
```

```

System.int ForceUpdateElectricalData2( 
   System.int Stream
)
```

```

System.int ForceUpdateElectricalData2( 
   System.int Stream
) 
```

#### Parameters

*Stream*
:   Stream as defined in swElectricalStreamType\_e

#### Return Value

Status of update as defined in swForceUpdateElectricalDataError\_e

Remarks

Third-party applications should use this method to tell the SOLIDWORKS software that they have changed the electrical data. The SOLIDWORKS software then re-reads the data to get the updates.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
