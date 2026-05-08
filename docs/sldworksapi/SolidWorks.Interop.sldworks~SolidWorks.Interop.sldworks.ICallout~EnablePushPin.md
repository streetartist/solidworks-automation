# EnablePushPin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~EnablePushPin`

Gets or sets whether to enable the pushpin for this callout.
Gets or sets whether to enable the pushpin for this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnablePushPin As System.Boolean
```

```

Dim instance As ICallout
Dim value As System.Boolean
 
instance.EnablePushPin = value
 
value = instance.EnablePushPin
```

```

System.bool EnablePushPin {get; set;}
```

```

property System.bool EnablePushPin {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable the callout pushpin, false to disable it

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)
