# Merge Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Merge`

Gets or sets whether to merge the results of the extrude feature in a multibody part.
Gets or sets whether to merge the results of the extrude feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Merge As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.Merge = value
 
value = instance.Merge
```

```

System.bool Merge {get; set;}
```

```

property System.bool Merge {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True enables the merge results option, false disables it

Remarks

The merge results option tells the SOLIDWORKS software whether or not to merge the  
new body or bodies with existing bodies in the multibody part. This property is set  
to True by default.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
