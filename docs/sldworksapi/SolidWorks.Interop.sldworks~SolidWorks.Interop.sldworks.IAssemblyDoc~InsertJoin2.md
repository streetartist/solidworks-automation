# InsertJoin2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertJoin2`

Constructs a feature from merged selected components.
Constructs a feature from merged selected components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertJoin2( _
   ByVal HideParts As System.Boolean, _
   ByVal ForceContact As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim HideParts As System.Boolean
Dim ForceContact As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertJoin2(HideParts, ForceContact)
```

```

System.bool InsertJoin2( 
   System.bool HideParts,
   System.bool ForceContact
)
```

```

System.bool InsertJoin2( 
   System.bool HideParts,
   System.bool ForceContact
) 
```

#### Parameters

*HideParts*
:   True hides the original components after the join is complete, false shows them

*ForceContact*
:   True joins any coincident faces and intruding volumes, false does not

#### Return Value

True if feature creation was successful, false if it was not

Remarks

When you use this method, SOLIDWORKS must be in Edit Part mode for the target part. You must also preselect the component parts to be merged into the edited part.

Example

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)  
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)  
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)
