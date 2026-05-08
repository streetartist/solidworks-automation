# LeaderBendLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~LeaderBendLength`

Gets the length of the unbent portion of the leader to this PMI datum.
Gets the length of the unbent portion of the leader to this PMI datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LeaderBendLength As System.Double
```

```

Dim instance As IPMIDatumFeature
Dim value As System.Double
 
instance.LeaderBendLength = value
 
value = instance.LeaderBendLength
```

```

System.double LeaderBendLength {get; set;}
```

```

property System.double LeaderBendLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of the unbent portion of the PMI datum leader

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.md)  
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.md)
