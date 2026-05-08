# Consume Property (ISplitBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume`

Gets or sets whether the bodies in this Split feature are consumed.
Gets or sets whether the bodies in this Split feature are consumed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Consume As System.Boolean
```

```

Dim instance As ISplitBodyFeatureData
Dim value As System.Boolean
 
instance.Consume = value
 
value = instance.Consume
```

```

System.bool Consume {get; set;}
```

```

property System.bool Consume {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the Split bodies are consumed, false if not

Remarks

Consumed means the split bodies are removed from the part and do not appear in the Solid Bodies folder of the FeatureManager design tree.

Example

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)  
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)  
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[IFeatureManager::PostSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md)  
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md)
